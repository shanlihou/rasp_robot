import RPi.GPIO as GPIO
import time

# 设置GPIO的编码方式
GPIO.setmode(GPIO.BCM)
# 设置GPIO脚号为输入模式，并启用内部上拉电阻
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

_set = set()

# 定义NEC协议解码函数
def decode_nec(pin):
    pulse = 0
    start = time.time()
    start_bit = False
    address = command = 0
    bits = 0

    while True:
        pulse = GPIO.input(pin)
        if pulse == GPIO.HIGH:
            pulse_length = time.time() - start
            if start_bit:
                if pulse_length > 0.0 and pulse_length < 0.001:  # 检查脉冲长度是否在NEC协议的逻辑"1"范围内
                    bit = int(pulse_length * 1000000)  # 将时间转换为微秒
                    if bit == 562:  # 逻辑"1"
                        command |= (1 << bits)
                    elif bit == 1690:  # 逻辑"0"
                        command |= (0 << bits)
                    bits += 1
                    if bits >= 32:  # NEC协议的地址和命令位总共32位
                        return address, command
            else:
                start_bit = True
                address = int(pulse_length * 1000000)  # 地址位
                bits = 16  # 地址位16位
        start = time.time()

# 红外信号接收函数
def read_ir_signal(pin):
    _num = 0
    try:
        while True:
            address, command = decode_nec(pin)
            _num = (_num << 8) | (address & 0xff)
            _num = 0xffffffff & _num
            if _num not in _set:
                _set.add(_num)
                print(f"NEC IR Signal: Address={address},{address:08b}, Command={command:016b}, _num={_num}")

            #if address != 1 and address != 0:
            #    print(f"NEC IR Signal: Address={address},{address:08b}, Command={command:016b}")
    except KeyboardInterrupt:
        GPIO.cleanup()

# 主函数
def main():
    read_ir_signal(21)

if __name__ == '__main__':
    main()
