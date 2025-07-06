# Discord M3U8 Audio Streamer Bot

A simple Discord bot that joins your voice channel and streams audio from any given M3U8 (HLS) link.  
Powered by [discord.py](https://github.com/Rapptz/discord.py) and FFmpeg.

---

## Features

- `/join <m3u8_url>` — Joins the voice channel you're currently in and streams audio from the specified M3U8 link.
- `/leave` — Leaves the voice channel.

---

## Commands

### `/join <m3u8_url>`

- **Description:** Join your current voice channel and start streaming audio from the given M3U8 URL.
- **Usage:**  
  `/join https://example.com/stream/playlist.m3u8`
- **Note:** You must be connected to a voice channel for this command to work.

### `/leave`

- **Description:** Disconnects the bot from the voice channel.

---

## Setup & Usage

### Prerequisites

- Python 3.8 or higher
- [FFmpeg](https://ffmpeg.org/download.html) installed and added to your system PATH
- A Discord bot token
- Your Discord server (guild) ID for command registration

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/discord-m3u8-streamer.git
   cd discord-m3u8-streamer
   ```

2. Create a virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
3. Install dependencies
   ```bash
    pip install -r requirements.txt
    ```
4. Create a .env file in the root folder with:
   ```
    BOT_TOKEN=your_bot_token_here
    GUILD_ID=your_guild_id_here
   ```

### Running the Bot
```bash
python dot.py
```


