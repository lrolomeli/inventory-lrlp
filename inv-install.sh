sudo apt update
sudo apt upgrade -y
sudo apt install python3.10 -y
sudo apt install python3-pip -y
pip install pyside2
sudo apt install mysql-server -y
echo -e "[mysql]\nuser=root\npassword=root\n\n[mysqldump]\nuser=root\npassword=root" > ~/.my.cnf
sudo mysql_secure_installation
mysql -u root inventariodb < inventariodb.sql
sudo apt install -f
