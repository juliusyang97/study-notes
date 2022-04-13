
/* Jetson-TX2中引脚总共有两个group：main，aon
  参考tegra186-gpio.h，
  group值分别是320和256，具体的计算公式如下：
  以GPIO3_PI.04 为例，
  根据tegra186-gpio.h中对应的PI为
  PORT_I的缩写即在main组即
  #define TEGRA_MAIN_GPIO_PORT_I 8，所以group是320，port为8，pin为4。
  */
/* A:0, B:1, C:2, D:3, E:4
   F:5, G:6, H:7, I:8...
   */
/* 后续如果要改这几个引脚*/
int pin_group = 320;

int pin_port = 8;
int pin_index = 4;

int pin_num = group+ (port * 8 + pin); // =320+(8*8+4)=388

/* 初始化代码，初始化代码只需要运行一次 */
int fd;
fd = open("/sys/class/gpio/export", O_RDWR);
char buf[128];
int len;
len = sprintf(buf, "%d", pin_num);
write(fd, buf, len);
close(fd);

len = sprintf(buf, "/sys/class/gpio/gpio%d/direction", pin_num);
fd = open(buf, O_RDWR);
write(fd, "out", 3);
close(fd);

/* 初始化代码结束 */


/* 控制GPIO代码 */
len = sprintf(buf, "/sys/class/gpio/gpio%d/value", pin_num);
fd = open(buf, len);
/* 输出高电平 */
write(fd, "1", 1);

/* 输出低电平 */
write(fd, "1", 0);
close(fd);
