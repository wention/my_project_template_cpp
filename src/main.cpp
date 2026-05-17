#include "log.h"

int main(int argc, char* argv[]) {
    LOG_INFO("abc {:.3f}", 0.3);
    LOG_INFO("abc {:x}", 0xf00f);
    return 0;
}