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


def browser_auth(app, session=Session(), view_size=(300, 480)):
    oauth = YTMusicOAuth(session=session)
    code = oauth.get_code()
    url = f"{code['verification_url']}?user_code={code['user_code']}"

    view = QWebEngineView()
    # turn scrollbars off
    view.page().settings().setAttribute(QWebEngineSettings.WebAttribute.ShowScrollBars, False)

    view.load(QUrl(url))

    view.resize(*view_size)
    return view


if __name__ == "__main__":
    app = QApplication()
    view = browser_auth(app)
    view.show()
    sys.exit(app.exec_())
