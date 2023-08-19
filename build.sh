cd hexo/hexo
yarn install
yarn run clean
yarn run build

rm -rf /opt/website/python4office.cn/*
cp /opt/workplace/pro/python4office.cn/hexo/hexo/public/* /opt/website/python4office.cn/ -R