import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication
from requests import Session
from ytmusicapi.auth.oauth import YTMusicOAuth

ROOT_PATH = Path(__file__).parent
OAUTH_PATH = ROOT_PATH / ".oauth"

OAUTH_PATH.mkdir(exist_ok=True)


def browser_auth(session=Session(), view_size=(300, 480)):
    oauth = YTMusicOAuth(session=session)
    code = oauth.get_code()
    url = f"{code['verification_url']}?user_code={code['user_code']}"

    view = QWebEngineView()
    # turn scrollbars off
    view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.ShowScrollBars, False)

    def url_changed(new_url: QUrl):
        if "done?authuser=0" in new_url.toString():
            print("Login success!")
            view.close()

            token = oauth.get_token_from_code(code["device_code"])
            oauth.dump_token(token, str(OAUTH_PATH / "oauth.json"))

    view.urlChanged.connect(url_changed)

    view.load(QUrl(url))

    view.resize(*view_size)
    return view


if __name__ == "__main__":
    app = QApplication()
    view = browser_auth()
    view.show()
    sys.exit(app.exec_())
