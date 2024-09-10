# fishregression

### Model Selection
##### 1차 회귀모형 (score : 0.922)
<img src="https://github.com/user-attachments/assets/977093c3-07da-438a-a687-0b0bea60b9f9" width="30%" />

##### 2차 회귀모형 (score : 0.967)
<img src="https://github.com/user-attachments/assets/3cfc68a1-c42b-4789-ae4e-4dc3b488aaea" width="30%" />

##### 3차 회귀모형 (score : 0.969)
<img src="https://github.com/user-attachments/assets/e865dab4-220c-4250-b078-1be6f8c44e9c" width="30%" />

> 1차 회귀모형보다 2차 회귀모형이 score가 높았고
> 2차 회귀모형과 3차 회귀모형의 score는 비슷하므로 2차 회귀모형이 좋음
> plot상에서도 2차 회귀모형이 가장 설명을 잘 하는 것으로 보이므로 2차 회귀모형 선택

### Usage
1. [mingk42/fish_classifier](https://hub.docker.com/repository/docker/mingk42/fish_classifier/general)를 pull합니다.
> `docker pull mingk42/fish_classifier:v1.6.8`
2. [mingk42/fish_regression](https://hub.docker.com/repository/docker/mingk42/fish_regression/general)를 pull합니다.
> `docker pull mingk42/fish_regression:v0.5.0`
3. `mingk42/fish_classifier`를 8002포트로 run합니다.
> `sudo docker run -d -p 8002:8080 --name fish_classifier mingk42/fish_classifier:v1.6.8`
4. `mingk42/fish_regression`를 8001포트로 run합니다. 
>`sudo docker run -d -p 8001:8080 --name fish_regression mingk42/fish_regression:v0.5.0`
5. [Repo](https://github.com/Mingk42/fishRegression/tree/v0.5.0/api_merge)를 install합니다.
> `pip install git+https://github.com/Mingk42/fishRegression.git@v0.5.0/api_merge`
6. `fish-predict`를 입력합니다.
7. 길이를 입력합니다.
8. 완료!

### Result
![image](https://github.com/user-attachments/assets/b44ac187-1b26-40a3-b933-930c7af98176)

### Exception
![image](https://github.com/user-attachments/assets/ea73c84d-3faf-4b1f-b60f-990a11af5bef)
> 길이가 작은 경우(<10.35) 음수의 무게가 나타나, 예측할 수 없다는 문구로 대체하였습니다.
> 2차 모형이다 보니 무게가 기하급수적으로 크게 추정되는 경향이 있는 것 같습니다.

### Dependency
![scikit-learn>=1.5.1](https://img.shields.io/badge/scikit--learn>=1.5.1-F7931E.svg?style=for-the-badge&logo=scikitlearn&logoColor=FFFFFF)

![fastapi>=0.114.0](https://img.shields.io/badge/fastapi>=0.114.0-009688.svg?style=for-the-badge&logo=fastapi&logoColor=FFFFFF)
