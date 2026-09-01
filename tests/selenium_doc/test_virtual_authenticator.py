import pytest
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions
from base64 import urlsafe_b64decode
from selenium.webdriver.common.virtual_authenticator import Credential

def test_add_and_remove_virtual_authenticator(driver):
    options = VirtualAuthenticatorOptions()

    driver.add_virtual_authenticator(options)
    assert driver.virtual_authenticator_id is not None
    assert driver.get_credentials() == []


    driver.remove_virtual_authenticator()
    assert driver.virtual_authenticator_id is None

def test_get_credentials_after_authenticator_removed(driver):
    options = VirtualAuthenticatorOptions()
    driver.add_virtual_authenticator(options)
    driver.remove_virtual_authenticator()

    with pytest.raises(ValueError):
        driver.get_credentials()

def test_configure_resident_authenticator(driver):
    options = VirtualAuthenticatorOptions(
        protocol=VirtualAuthenticatorOptions.Protocol.CTAP2,
        has_resident_key=True,
        has_user_verification=True,
        is_user_verified=True
    )
    driver.add_virtual_authenticator(options)
    assert driver.virtual_authenticator_id is not None
    driver.remove_virtual_authenticator()
    assert driver.virtual_authenticator_id is None

def test_add_real_residential_key(driver):
    TEST_PRIVATE_KEY_B64 = (
        "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQg8_zMDQDYAxlU-Q"
        "hk1Dwkf0v18GZca1DMF3SaJ9HPdmShRANCAASNYX5lyVCOZLzFZzrIKmeZ2jwU"
        "RmgsJYxGP__fWN_S-j5sN4tT15XEpN_7QZnt14YvI6uvAgO0uJEboFaZlOEB"
    )
    options = VirtualAuthenticatorOptions(
        protocol=VirtualAuthenticatorOptions.Protocol.CTAP2,
        has_resident_key=True,
        has_user_verification=True,
        is_user_verified=True,
    )
    driver.add_virtual_authenticator(options)
    credential_id = b"\x01\x02\x03\x04"
    rp_id = "localhost"
    user_handle = b"\x01"
    private_key = urlsafe_b64decode(TEST_PRIVATE_KEY_B64)
    sign_count = 0
    credential = Credential.create_resident_credential(
        credential_id,
        rp_id,
        user_handle,
        private_key,
        sign_count
    )
    driver.add_credential(credential)
    credentials = driver.get_credentials()

    assert len(credentials) == 1
    assert credentials[0].id == credential.id
    driver.remove_credential(credential.id)
    assert driver.get_credentials() == []

    driver.remove_virtual_authenticator()

def test_remove_all_credentials(driver):
    TEST_PRIVATE_KEY_B64 = (
        "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQg8_zMDQDYAxlU-Q"
        "hk1Dwkf0v18GZca1DMF3SaJ9HPdmShRANCAASNYX5lyVCOZLzFZzrIKmeZ2jwU"
        "RmgsJYxGP__fWN_S-j5sN4tT15XEpN_7QZnt14YvI6uvAgO0uJEboFaZlOEB"
    )
    options = VirtualAuthenticatorOptions(
        protocol=VirtualAuthenticatorOptions.Protocol.CTAP2,
        has_resident_key=True,
        has_user_verification=True,
        is_user_verified=True,
    )
    driver.add_virtual_authenticator(options)
    rp_id = "localhost"
    user_handle = b"\x01"
    private_key = urlsafe_b64decode(TEST_PRIVATE_KEY_B64)
    sign_count = 0
    credential_id = b"\x01\x02\x03\x04"
    credential_id_2 = b"\x05\x06\x07\x08"
    user_handle_2 = b"\x02"
    credential = Credential.create_resident_credential(
        credential_id,
        rp_id,
        user_handle,
        private_key,
        sign_count
    )
    credential_2 = Credential.create_resident_credential(
        credential_id_2,
        rp_id,
        user_handle_2,
        private_key,
        sign_count
    )
    driver.add_credential(credential)
    driver.add_credential(credential_2)
    credentials = driver.get_credentials()
    assert len(credentials) == 2
    driver.remove_all_credentials()
    assert driver.get_credentials() == []
    driver.remove_virtual_authenticator()







