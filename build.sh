pyinstaller ./index.spec

cp -r ./app/data ./dist/data
cp -r ./app/images ./dist/images

