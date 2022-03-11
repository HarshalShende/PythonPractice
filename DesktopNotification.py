from plyer import notification
import time

if __name__=='__main__':
    while True:
        notification.notify(
            title="*** Take Some Rest ***",
            message="Let Your Mind Be Free From Frustration & Reduce eyestrain",
            app_icon="D:/notification/try.ico",
            timeout=5)
        time.sleep(10)