---
title: I Stayed Up All Night and Built a Free-for-Life Voice Input Tool with Trae
date: 2026-06-07 00:00:00
tags: [AI Tools, Voice Input, Open Source, Tauri, macOS]
categories: [AI Tools]
keywords: [VoiceInput, voice input, AI tools, open source, Tauri, macOS voice input]
description: I stayed up all night and built a macOS voice input tool with Tauri — permanently free, open source, and ready for anyone to use.
cover: https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop
translation:
  source: /Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ai/20260607-voice-input-open-source.md
  status: completed
  translator: ai-claude-gpt4
  translated_at: 2026-06-14T10:00:00Z
---

<!-- more -->

# I Stayed Up All Night and Built a Free-for-Life Voice Input Tool

Last night, I just couldn't take it anymore.

Voice input tools on the market today — they all want you to log in, or pay for a membership; they limit usage count, or they cap duration.

Some start out saying they're free, then pop up paywalls once you're hooked.

The worst part: all you want is to convert your voice to text, but you get blocked by every kind of third-party service.

So I just stayed up all night and built one myself.

The name is simple: **VoiceInput**.

It's a voice input tool for macOS.

You place your cursor in any input field, press a hotkey to start speaking, press it again to stop — it automatically transcribes what you said into text and pastes it into the active window.

The default hotkey is:

> Option + K

The whole flow is dead simple:

1. Place your cursor where you want to type
2. Press `Option + K` to start recording
3. When done, press `Option + K` again
4. Speech is auto-recognized as text
5. Auto-copied to clipboard, and pasted into the current input field if permission allows

This isn't a demo. The full pipeline is already working:

- Always-on menu bar icon
- Global hotkey to start recording
- Microphone audio capture
- Real-time speech recognition
- Floating panel at the bottom showing status
- Recognized text written to clipboard
- Auto-paste into the current app when permission is granted
- Manual `Cmd + V` fallback when auto-paste permission isn't available

That means you can use it directly in WeChat, Feishu, browsers, code editors, and documents.

You speak. It types.

That's exactly what I wanted.

## Why Did I Build It Myself?

The reason is simple: I refuse to be held hostage by third parties any longer.

Voice input should be a basic capability.

Every day, when you write messages, write documents, write articles, or jot down inspiration — often it's not that you can't write, it's that you're too lazy to type.

Especially for long text, typing is just too slow.

But many voice input tools have overcomplicated this:

- Require account registration
- Require paid membership
- Limit usage count
- Force-bind to a specific platform
- Pile on features you don't want

All I want to do is say something, and have it become text.
