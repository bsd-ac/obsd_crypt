from obsd_crypt import crypt_checkpass


def test_checkpass():
    prebuilt_hashes = {
        'de3830bb3b1b007d309ea617':
        '$2b$10$UTZyAgc0fJcCb8Ws8eENwOH70RD772m1BK4JdzifXU.Zz562Qiy7e',
        '1878dda21bd49d8b32f342b3':
        '$2b$10$zzqaG6QnOJ4N92vgG8uNdefpC5Rc0aP8nnz0NQQs4KhgzpxRRXK0y',
        'e92dee88b1306ef5ef3e4ab5':
        '$2b$10$GDK.7V.E9Y6XQrbCftdMW.gahjJcwC1MbrBYp99npBdp.bGn0bDgC',
        'dc3ed5be6ce39e0edfc7b506':
        '$2b$10$q1ODItamxLtEOlRubAi5Su6O19o7Rszowd6kd1aZIh4NEm3uqQ0om',
        '4cb42bb2744cfc74d8d6e761':
        '$2b$10$/PmI5Tbj3aXoZw8Be.MyCe436BaTObnOrEoOfnY3YcnJSamCEa9ge',
        'c31765e3b57400a01abfa2a3':
        '$2b$10$OrwzXl282s8DK7e0F5lu7eEaX3RZHGUuQ9D2KiY40q6MEkSgxSUFS',
        '604e0d5a64205b63788e6b44':
        '$2b$10$BuwBA76L2NbFlokyA064Z.yH67kgHo6XEEtgNUTM6eiMdyi/MOjvK',
        'f50eb0e6851ad01698280771':
        '$2b$10$eYaf5rfZuwRenjxMbVuf1u.z4ZpcOygfoSbM8Tq9FNT5PMdG7lVUq',
        '326fd188187127958aa3276a':
        '$2b$10$b.w5oK2//XUIjAvXhb4thuADZccgIzeMlmKlGMzkz6cXG9qK0E9E6',
        '1b092fc30f91ed7c5ae559a3':
        '$2b$10$qfj5srotJbijCsDHLTL7E.XAy54.ilW5ucwnslwAqwfooW0GMPKMu',
        'b1dd8eea0d9f338ee4382446':
        '$2b$10$JU1VweX7K5OzI0D7ktHAfuKfy1ltNGD0DlVLDLae0I4baOwpJaYIq',
        '2f9c8d85b51bdd19d04665ac':
        '$2b$10$iOJGLie4yssYbZ/W9UdvAeXlVycl/yewyQzF/8SZnA3Yc0PjmbdNm',
        '8cecb847219e3883e69caad0':
        '$2b$10$Yqmwl3/HV5p0HekfIlCv1OIqMQqwkV3k3lweiAvXiCxdg7wtUqt7m',
        'bc25e947b0e547cd5c3e0608':
        '$2b$10$l7QrUqyJEOAx.hfb/s5qvuYLgRbtoDqDsol3yHczvn0CvXVSa2f6q',
        '8a02dbb7ef1f59bfe3960e87':
        '$2b$10$35lEM7/mA2BgynFioqqYNurvmxUHyK.daBCuzh1l467NwHPvDB7Bm',
    }
    for password, password_hash in prebuilt_hashes.items():
        assert (crypt_checkpass(password, password_hash))
