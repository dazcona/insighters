build:
	docker-compose -f docker/docker-compose.yml build
run:
	docker-compose -f docker/docker-compose.yml run face_recon bash
connect:
	ssh -i data/hackathon-2018-team-3  hackathon-2018-team-3@35.240.31.61