echo "Are You sure to delete your Project? this cannot be undone! [Y/n]"
read option
if [ "$option" == "Y" ] || [ "$option" == "y" ]
then
    dirname=/$PWD
    shopt -s extglob           # enable +(...) glob syntax
    result=${dirname%%+(/)}    # trim however many trailing slashes exist
    result=${result##*/}       # remove everything before the last / that still remains
    result=${result:-/}        # correct for dirname=/ case
    printf '%s\n' "$result"
    if [ "$result" == "$USER" ]
    then
        echo "you tried to delete a home directory, aborting..."
        exit 1;
    fi
    cd ..
    sudo rm -rf $result
fi