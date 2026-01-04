<!-- pwd && ls -la && mkdir github && cd github && git clone https://github.com/vuvannghiawork/jenkins-example-docker-compose && cd jenkins-example-docker-compose && cd start && chmod +x add_key.sh && ./add_key.sh && tail -n 1 ~/.ssh/authorized_keys -->

<!-- pwd && ls -la && mkdir github && cd github && git clone https://github.com/vuvannghiawork/jenkins-example-docker-compose && cd jenkins-example-docker-compose && cd jenkins && docker compose -f docker-compose.yml up -d -->


<!-- python3 -m http.server 8000 -->
<!-- https://github.com/vuvannghiawork/jenkins-example-docker-compose -->
<!-- docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword -->

<!-- 6dddc2fb6c61418ea54d9914ed8aef6e -->

echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC7UzAYJVgXJgN1d1NrgjAxoKOwAAYfGDfPxPRaJS5ViiQIP0XXLZeUbrrlPksXU6j63APuIr2wn3AvSIF+39NGkvmksLBBl/PPme7Nwa/mKTxNkt9nAvOGzMdAoQ8laEmkSYRdH85eX3yM3Tmeu3g1T54wGtPAjRP7ANA3zgPBVwrSVJEZguVnl9DerfmYQUF8y4HPmPArR9mmRMXQlQqn45V7ytWY2B59SmnUDiL+/6zJVjLMrJdobz7OcfSgokS1kbNrizIKGOifcV+uQyh2iw7u7K2pz4nzvnBp2b7cNM1f59BXkfJHhPtTvkfUYyXshBZ+qFMdDW5314oP3noZ5O2JNl02QucMN3St5Vvl3oYHaJ0bN9nxy/v1X1v+WSzjQwQo/MR9qK8vbBmxhiN9X1RPNXU27n+UfqRIOfBj1UYokfcBQ+rU0nNQgf6PX2N5B067SDnyZS6XtbD+t3BCnLh1EfsOxFWgRV+aN12lpWdv6CaWfT+HR1Y75Aka7cxwgDsBaUk5ElSvkX1flwhXoeeiDpRb7S7dugPyPSVPYMzGQURiZfHrWMbou1bEpChzRMBZcMmgtPojzG4t5GNLSJ0zmFdscK86W751or94hA34evVrFSHD9cvWu7AQchODSawxIulrYKHnxCIQe4sxLFb3jI9sJwNi0qvdyn1CGQ== Admin@DESKTOP-8S38TS9" >> ~/.ssh/authorized_keys

ssh -o PubkeyAcceptedAlgorithms=+ssh-rsa ip172-18-0-10-d5d7cd291nsg00bshhag@direct.labs.play-with-docker.com

cat <<EOF > ~/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC7UzAYJVgXJgN1d1NrgjAxoKOwAAYfGDfPxPRaJS5ViiQIP0XXLZeUbrrlPksXU6j63APuIr2wn3AvSIF+39NGkvmksLBBl/PPme7Nwa/mKTxNkt9nAvOGzMdAoQ8laEmkSYRdH85eX3yM3Tmeu3g1T54wGtPAjRP7ANA3zgPBVwrSVJEZguVnl9DerfmYQUF8y4HPmPArR9mmRMXQlQqn45V7ytWY2B59SmnUDiL+/6zJVjLMrJdobz7OcfSgokS1kbNrizIKGOifcV+uQyh2iw7u7K2pz4nzvnBp2b7cNM1f59BXkfJHhPtTvkfUYyXshBZ+qFMdDW5314oP3noZ5O2JNl02QucMN3St5Vvl3oYHaJ0bN9nxy/v1X1v+WSzjQwQo/MR9qK8vbBmxhiN9X1RPNXU27n+UfqRIOfBj1UYokfcBQ+rU0nNQgf6PX2N5B067SDnyZS6XtbD+t3BCnLh1EfsOxFWgRV+aN12lpWdv6CaWfT+HR1Y75Aka7cxwgDsBaUk5ElSvkX1flwhXoeeiDpRb7S7dugPyPSVPYMzGQURiZfHrWMbou1bEpChzRMBZcMmgtPojzG4t5GNLSJ0zmFdscK86W751or94hA34evVrFSHD9cvWu7AQchODSawxIulrYKHnxCIQe4sxLFb3jI9sJwNi0qvdyn1CGQ== Admin@DESKTOP-8S38TS9
EOF
chmod 600 ~/.ssh/authorized_keys


ssh-keygen -t ed25519 -C "vuvannghia.work@gmail.com"