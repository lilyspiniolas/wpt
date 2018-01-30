from tests.support.asserts import assert_error, assert_same_element, assert_success
from tests.support.inline import inline


def element_send_keys(session, element, text):
    return session.transport.send(
        "POST",
        "/session/{session_id}/element/{element_id}/value".format(
            session_id=session.session_id,
            element_id=element.id),
        {"text": text})



def test_input_append(session):
    session.url = inline("<input value=a>")
    element = session.find.css("input", all=False)
    assert element.property("value") == "a"

    element_send_keys(session, element, "b")
    assert element.property("value") == "ab"

    element_send_keys(session, element, "c")
    assert element.property("value") == "abc"


def test_textarea_append(session):
    session.url = inline("<textarea>a</textarea>")
    element = session.find.css("textarea", all=False)
    assert element.property("value") == "a"

    element_send_keys(session, element, "b")
    assert element.property("value") == "ab"

    element_send_keys(session, element, "c")
    assert element.property("value") == "abc"
