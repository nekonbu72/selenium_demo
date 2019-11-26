from download import download_dir
from userprofile import profile_dir


class Config:
    MIME_TYPES = ["application/epub+zip",
                  "application/gzip",
                  "application/java-archive",
                  "application/json",
                  "application/ld+json",
                  "application/msword",
                  "application/octet-stream",
                  "application/ogg",
                  "application/pdf",
                  "application/rtf",
                  "application/vnd.amazon.ebook",
                  "application/vnd.apple.installer+xml",
                  "application/vnd.mozilla.xul+xml",
                  "application/vnd.ms-excel",
                  "application/vnd.ms-fontobject",
                  "application/vnd.ms-powerpoint",
                  "application/vnd.oasis.opendocument.presentation",
                  "application/vnd.oasis.opendocument.spreadsheet",
                  "application/vnd.oasis.opendocument.text",
                  "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                  "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                  "application/vnd.visio",
                  "application/x-7z-compressed",
                  "application/x-abiword",
                  "application/x-bzip",
                  "application/x-bzip2",
                  "application/x-csh",
                  "application/x-freearc",
                  "application/xhtml+xml",
                  "application/xml",
                  "application/x-rar-compressed",
                  "application/x-sh",
                  "application/x-shockwave-flash",
                  "application/x-tar",
                  "application/zip",
                  "appliction/php",
                  "audio/aac",
                  "audio/midi audio/x-midi",
                  "audio/mpeg",
                  "audio/ogg",
                  "audio/wav",
                  "audio/webm",
                  "font/otf",
                  "font/ttf",
                  "font/woff",
                  "font/woff2",
                  "image/bmp",
                  "image/gif",
                  "image/jpeg",
                  "image/png",
                  "image/svg+xml",
                  "image/tiff",
                  "image/vnd.microsoft.icon",
                  "image/webp",
                  "text/calendar",
                  "text/css",
                  "text/csv",
                  "text/html",
                  "text/javascript",
                  "text/javascript",
                  "text/plain",
                  "text/xml",
                  "video/3gpp",
                  "video/3gpp2",
                  "video/mp2t",
                  "video/mpeg",
                  "video/ogg",
                  "video/webm",
                  "video/x-msvideo"]

    FIREFOX = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

    GECKODRIVER = "geckodriver.exe"

    LOG = "log\\gecko.log"

    USER_DEFINED = 2

    DOWNLOAD = download_dir()
    if DOWNLOAD is None:
        raise Exception("ProfileNotExistError")

    PREFERENCE = {"browser.download.useDownloadDir": True,
                  "browser.helperApps.neverAsk.saveToDisk": ",".join(MIME_TYPES),
                  "browser.download.folderList": USER_DEFINED,
                  "browser.download.lastDir": "",
                  "browser.download.dir": DOWNLOAD}

    PROFILE = profile_dir()
    if PROFILE is None:
        raise Exception("ProfileNotExistError")
