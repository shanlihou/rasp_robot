import RPi.GPIO as GPIO
import time

# 设置GPIO的编码方式
GPIO.setmode(GPIO.BCM)

# 设置GPIO脚号为输入模式
GPIO.setup(21, GPIO.IN)

# 红外信号接收函数
def read_ir_signal(pin):
    while True:
        if GPIO.input(pin):  # 如果引脚被设置为高电平
            print("IR signal detected")
            time.sleep(0.1)  # 等待一段时间，避免抖动

# 主函数
def main():
    try:
        # 读取红外信号
        read_ir_signal(21)
    except KeyboardInterrupt:
        # 处理Ctrl+C的情况
        GPIO.cleanup()  # 清理GPIO设置
        print("Program exited cleanly")

if __name__ == '__main__':
    main()
