from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message_odd():
    assert encrypt_message('feijão', 3) == 'ief_oãj'


def test_encrypt_message_even():
    assert encrypt_message('feijão', 4) == 'oã_jief'


def test_encrypt_message_with_invalid_index():
    assert encrypt_message('feijão', -1) == 'oãjief'
