# import logging

# # debug < info < warning < error < critical
# # logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# logging.debug("이거 누가 한거야~~")
# logging.info("자동화수행준비")
# logging.warning("경고경고")
# logging.error("에러발생")
# logging.critical("복구불가한 에러 발생")



import logging
from datetime import datetime
#시간[로그레벨] 메시지 형태 로그 작성문
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()

#로그 레벨 설정
logger.setLevel(logging.DEBUG)

#스트림(터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter) 
logger.addHandler(streamHandler)

#파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남기는 테스트를 진행")
