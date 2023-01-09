#extract urls/keywords from mongodb
python3 getUrls.py > urls 2> urls.err

#download images
cat urls | cut -d\; -f1 | while read i; do j=$(echo $i|sed 's|.*/||;s|\s*||g'); [[ -f "img/$j" ]] || wget -O "img/$j" "$i"; done

# check if images are unique
md5sum img/* > urls.md5
wc -l urls.md5
19288 
awk '{print $1}' urls.md5 |sort  -u | wc -l
19265

#prepare curation assignments
perl -e 'open U, "urls"; while (<U>){chop();($u, $q, $t) = split(/;/);$q=~tr/[A-Z]/[a-z]/;@qq=split(/ /,$q);next if length($qq[0]) < 2 || length($qq[1]) < 2; $q=~s/ -site:.*//;@p=split(/\//, $u, -1);$f2d{$p[$#p]}="$q;$u";} for $f (keys %f2d){print "$f;$f2d{$f}\n";}' > f2d
# make sure image has been downloaded
cat f2d | while IFS=\; read f k u; do [[ -f img/$f ]] && echo $f";"$k";"$u; done | grep '\.jpg;' | sort -t\; -k2 > f2d1

#separate into individual assignments   
split -n l/105 -d f2d1 f2d.

#assignment files $i.img
ls f2d.* | paste students/ids.txt - | while read i j; do mv $j $i.img; done
scp -p img/* da2:/data/shared/fdac22/fruit_img/


echo "|netid|cluster labels|" > clusters.md
echo "|-|-|" >> clusters.md
cat students/ids.txt  | while read i; do echo "|$i|"$(cat $i.img | cut -d\; -f2 | sort -u|awk '{print $0" - "}')"|" ; done >> clusters.md

cat students/ids.txt  | while read i; do cat $i.img | cut -d\; -f2 ; done | sort -u | sed "s|^|'|;s|$|',|" > cls

cat *.img > import

#run containers (see icputrd.sh)


#apt install python3-pymongo

#time to import to database?
cat import | cut -d\; -f1,2 | sed 's|^|/fruit_img/|' | grep '\.jpg;' |python3 importCls.py

#edit /etc/sssd/sssd.conf 
ldap_uri = ldap://ldap.eecs.utk.edu
#ldap_id_use_start_tls = True

#edit /opt/mean.js/modules/clusters/client/controllers/cluster_images.client.controller.js
# to include tags from cls

#import to database
cat import | cut -d\; -f1,2 | sed 's|^|/fruit_img/|' | grep '\.jpg;' |python3 importCls.py



python3 listC.py | sed 's|//localhost:3000/fruit_img/||;s| |;|' > mapNow
#update
sort -t\;  mapNow | join -t\; -v1 - <(sort mapNow.11-06)| cut -d\; -f1 > bad
sort -t\;  mapNow | join -t\; - <(sort mapNow.11-06) | awk -F\; '{if ($2 != $4 || $3 != $5) print $0}' > newLabels
cat bad | python3 rmD.py
cat  newLabels   | python3 mvD.py 

docker run --gpus all  -it     -v /da2_data/shared/fdac22/fruit_img/:/img    -v /home/:/home/     --name fdacKERAS      tf-z  bash
apt update
apt install python3-pymongo python3-pandas

cd /
cat /home/audris/course/fdac22/Miniproject3/mapNow | python3 /home/audris/course/fdac22/Miniproject3/getResNetFeaturesGPU.py
