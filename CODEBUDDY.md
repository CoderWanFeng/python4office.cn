# CODEBUDDY.md This file provides guidance to CodeBuddy Code when working with code in this repository.

## Project Overview

This is a personal blog website built with **Hexo** static site generator, accessible at http://python4office.cn. The site contains technical articles, learning notes, and personal essays focused on Python automation and development.

## Architecture

### Core Structure
- **Root directory**: Contains project documentation and configuration
- **hexo/hexo/**: Main Hexo site directory with all content and configuration
- **themes/**: Multiple Hexo themes available (yilia, butterfly, icarus, next, replica)
- **source/_posts/**: Blog content organized by year/month

### Current Configuration
- **Active theme**: yilia (configured in _config.yml:106)
- **Language**: Chinese (zh-CN)
- **Post organization**: Posts are stored in `source/_posts/YYYY/` directories
- **Asset handling**: Post asset folders enabled for media files

## Development Commands

All commands should be run from the `hexo/hexo/` directory:

```bash
cd hexo/hexo/

# Install dependencies
yarn install

# Clean generated files
yarn run clean

# Build the site
yarn run build

# Start local development server
yarn run server

# Deploy (configure deployment settings first)
yarn run deploy
```

## Content Management

### Creating New Posts
Use Hexo's scaffolding system:
```bash
hexo new "Post Title"
```

Posts are created with asset folders for associated files. Content follows standard Hexo front-matter format.

### Theme Customization
- Multiple themes available in `themes/` directory
- Current active theme: yilia
- Theme configuration files are separate from main `_config.yml`

## Key Configuration Files

- `_config.yml`: Main Hexo configuration (site settings, URLs, plugins)
- `themes/[theme-name]/_config.yml`: Theme-specific settings
- `package.json`: Node.js dependencies and scripts
- `scaffolds/`: Post templates for different content types

## Deployment

Deployment is configured via Hexo's deploy settings in `_config.yml`. Currently uses git-based deployment. Sitemap generation is enabled for both Google and Baidu.

## Content Structure

Blog posts are organized by publication date in `source/_posts/YYYY/` directories. Each post can have associated assets in its own folder (enabled by `post_asset_folder: true`).