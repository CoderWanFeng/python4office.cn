cd /opt/workplace/pro/python4office.cn/hexo/hexo
yarn install
hexo clean
hexo g

rm -rf /opt/website/python4office.cn/*
cp /opt/workplace/pro/python4office.cn/hexo/hexo/public/* /opt/website/python4office.cn/ -R 