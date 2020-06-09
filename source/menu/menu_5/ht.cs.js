if [[ -f curso-html-css-js.pdf ]];then
rm curso-html-css-js.pdf
fi
read -p $'\e[1;32mInserta la ruta a guardar el curso(\e[1;39mEjemplo: /sdcard\e[1;32m)\e[1;39m > ' ruta
echo -e "\e[1;32m[*]\e[1;39m Descargando curso Html, Css, JS..."
wget https://gutl.jovenclub.cu/wp-content/uploads/2013/10/El%2Bgran%2Blibro%2Bde%2BHTML5%2BCSS3%2By%2BJavascrip.pdf -O curso-html-css-js.pdf -o log

if [[ -f log ]];then
rm log
fi
mv curso-html-css-js.pdf $ruta
clear
echo -e "\e[1;33m[*]\e[1;39m Curso guardado $ruta/curso-html-css-js.pdf"

