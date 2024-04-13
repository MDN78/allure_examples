import allure


@allure.id("31632")
@allure.title("Auth via Google(clone)")
@allure.tag("web", "smoke")
@allure.story("External Auth")
@allure.feature("Auth")
@allure.label("msrv", "Auth")
@allure.label("owner", "allure8")
def test_google_auth():
    with allure.step("Open main page"):
        pass
    with allure.step("Selec authorization method via Google"):
        pass
    with allure.step("Authorization as user 'random'"):
        with allure.step("Input LOGIN random@gmail.com"):
            pass
        with allure.step("Input PASSWORD 'random pass'"):
            pass
        with allure.step("Press button LogIn"):
            pass
    with allure.step("Checking success authorization"):
        pass
    with allure.step("Checking profile date was updated via Google"):
        with allure.step("Name: 'random'"):
            pass
        with allure.step("Email: 'random@gmail.com'"):
            pass