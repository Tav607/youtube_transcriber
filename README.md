# YouTube Audio Downloader

这个项目包含一个交互式脚本，帮助你从单个 YouTube URL 下载音频文件。默认下载 `webm` 音频流，不需要 `ffmpeg`；若选择其他格式，则会调用 `ffmpeg` 转码。

## 依赖

- Python 3.12+
- `yt-dlp`
- （可选）`ffmpeg`：当你选择非 `webm` 格式时需要

## 快速开始

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install yt-dlp
python download_audio.py
```

脚本启动后：
1. 输入想要下载的 YouTube 视频 URL。
2. 从列表中选择输出格式（默认是 `webm`）。
3. 文件会保存到 `output/` 目录，文件名使用视频标题。

## 常见问题

- **缺少 ffmpeg**：若在选择 `mp3`、`m4a` 等格式时提示缺少 `ffmpeg/ffprobe`，请先安装：`sudo apt install ffmpeg`。
- **下载失败**：YouTube 会定期调整接口，如果遇到解析错误，请先更新 `yt-dlp`：`pip install --upgrade yt-dlp`。

## 目录结构

- `download_audio.py`：交互式下载脚本。
- `output/`：默认的音频输出目录（可手动清理）。
- `README.md`：项目说明。
- `AGENTS.md`：自动化使用说明。
