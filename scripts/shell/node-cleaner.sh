docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker volume rm $(docker volume ls -q)

for mount in $(mount | grep tmpfs | grep '/var/lib/kubelet' | awk '{ print $3 }') /var/lib/kubelet /var/lib/rancher; do umount $mount; done

rm -rf /etc/ceph \
      /etc/cni \
      /etc/kubernetes \
      /opt/cni \
      /opt/rke \
      /run/secrets/kubernetes.io \
      /run/calico \
      /run/flannel \
      /var/lib/calico \
      /var/lib/etcd \
      /var/lib/cni \
      /