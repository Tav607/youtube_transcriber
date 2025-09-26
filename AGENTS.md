# Agent Playbook

## Goal
使用 `download_audio.py` 脚本，从指定的 YouTube URL 下载音频文件到 `output/` 目录。默认选择 `webm`，可按需切换到其他格式。

## Workflow
1. **准备环境**
   - 如果虚拟环境不存在，运行 `python3 -m venv .venv`。
   - 激活虚拟环境：`. .venv/bin/activate`。
   - 安装依赖：``pip install --upgrade pip`` 后运行 ``pip install -r requirements.txt``。
2. **运行脚本**
   - 执行 `python download_audio.py`。
   - 按提示输入 URL，并选择所需格式。
3. **后处理（可选）**
   - 如果使用非 `webm` 格式，请确认系统已安装 `ffmpeg`。
   - 下载出的文件位于 `output/`，按需处理或归档。

## Notes
- 如果脚本提示 `yt-dlp executable not found`，说明虚拟环境未激活或依赖未安装。
- `webm` 格式不会调用 `ffmpeg`，适合在没有多媒体工具的最小环境中使用。
- 如需批量处理，可在脚本基础上扩展循环或接受命令行参数。
