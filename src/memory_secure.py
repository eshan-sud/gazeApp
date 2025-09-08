# src/memory_secure.py

# memory-lock + DPAPI helpers

import ctypes

kernel32 = ctypes.windll.kernel32
VirtualLock = kernel32.VirtualLock
VirtualUnlock = kernel32.VirtualUnlock
VirtualLock.argtypes = (ctypes.c_void_p, ctypes.c_size_t)
VirtualUnlock.argtypes = (ctypes.c_void_p, ctypes.c_size_t)

def lock_bytes(b: bytes):
    # create a C buffer, copy bytes, lock memory pages (best-effort)
    buf = ctypes.create_string_buffer(b)
    addr = ctypes.addressof(buf)
    size = ctypes.c_size_t(len(b))
    ok = VirtualLock(ctypes.c_void_p(addr), size)
    if not ok:
        raise OSError("VirtualLock failed (insufficient privilege or quota)")
    # return buf (keep ref so memory stays allocated)
    return buf

def unlock_buf(buf):
    addr = ctypes.addressof(buf)
    size = ctypes.c_size_t(len(buf))
    VirtualUnlock(ctypes.c_void_p(addr), size)

import win32crypt

def save_encrypted(path, data_bytes):
    desc = "GazeApp calibration"
    encrypted = win32crypt.CryptProtectData(data_bytes, desc, None, None, None, 0)
    with open(path, "wb") as f:
        f.write(encrypted)

def load_encrypted(path):
    with open(path, "rb") as f:
        blob = f.read()
    decrypted = win32crypt.CryptUnprotectData(blob, None, None, None, 0)[1]
    return decrypted