import sys
sys.path.append('.')
import pyDH

def test_pydh_keygen():
    d1 = pyDH.DiffieHellman()
    d2 = pyDH.DiffieHellman()
    d1_pubkey = d1.gen_public_key()
    d2_pubkey = d2.gen_public_key()
    d1_sharedkey = d1.gen_shared_key(d2_pubkey)
    d2_sharedkey = d2.gen_shared_key(d1_pubkey)
    assert d1_sharedkey == d2_sharedkey
