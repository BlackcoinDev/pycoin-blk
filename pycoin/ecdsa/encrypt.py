def generate_shared_public_key(my_private_key, their_public_pair, generator):
    """
    Two parties each generate a private key and share their public key with the
    other party over an insecure channel. The shared public key can be generated by
    either side, but not by eavesdroppers. You can then use the entropy from the
    shared public key to created a common symmetric key for encryption. (This
    is beyond of the scope of pycoin.)

    See also <https://en.wikipedia.org/wiki/Key_exchange>

    :param my_private_key: an integer private key
    :param their_public_pair: a pair ``(x, y)`` representing a public key for the ``generator``
    :param generator: a :class:`Generator <pycoin.ecdsa.Generator.Generator>`
    :returns: a :class:`Point <pycoin.ecdsa.Point.Point>`, which can be used as a shared
        public key.
    """
    p = generator.Point(*their_public_pair)
    return my_private_key * p
