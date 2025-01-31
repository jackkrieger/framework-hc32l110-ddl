# PlatformIO support for HUADA HC32L110 DDL

This repository contains the [HUADA HC32L110 DDL](https://www.hdsc.com.cn), adapted to work with [PlatformIO](https://platformio.org/).


## Getting Started

to get started using the HC32L110 DDL, use the following in your `platformio.ini`:

```ini
[env:my_env]
platform = https://github.com/jackkrieger/platform-hc32l110.git
framework = ddl
board = generic_hc32l110x4
```

## License

new code added to the DDL framework is licensed under the [GPL-3.0](./LICENSE) license, while the original DDL code is licensed under the BSD 3-Clause license.
files licensed under the BSD 3-Clause license have a header at the top of the file, specifying the license.
