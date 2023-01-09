
# copied css and js to the container instead of mounting
# mounting /home to allow many to login

docker run -d \
    -v /data/shared/fdac22/fruit_img/:/opt/mean.js/public/fruit_img \
    -v /home/:/home/ \
    -p 3099:22 \
    --name fdacICPUTRD \
    --link dbFDAC:dbNew  icputrd/platform:fdac \
    /bin/startsvc.sh


# database
docker run -d --name dbFDAC icputrd/mongo:works



