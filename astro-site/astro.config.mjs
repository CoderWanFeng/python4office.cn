import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://www.python4office.cn/',
  integrations: [mdx()],
  output: 'static',
  build: {
    format: 'directory'
  }
});
