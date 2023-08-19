cd hexo/hexo
yarn install
yarn run clean
yarn run build

rm -rf /home/ubuntu/workplace/pro/website/python4office.cn/*
cp /home/ubuntu/workplace/pro/python4office.cn/hexo/hexo/public/* /home/ubuntu/workplace/pro/website/python4office.cn/ -R