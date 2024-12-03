cd hexo/hexo
yarn install
yarn run clean
yarn run build

git add .
git commit -m "update"
git push
#rm -rf /opt/website/python4office.cn/*
#cp /opt/workplace/pro/python4office.cn/hexo/hexo/public/* /opt/website/python4office.cn/ -R