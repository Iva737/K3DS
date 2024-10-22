#include <SFML/Graphics.hpp>
#include <string>
#include <iostream>

using namespace sf;
using namespace std;

struct Player {
    int x = 0;
    int y = 0;
};



int mx = 700; //Width  Window
int my = 700; //Height Window

void draw(){
    
}

int main(){
    // Создаем окно
    sf::RenderWindow window(sf::VideoMode(mx, my), "Context Finder");
    
    // Создаем круг
    sf::CircleShape circle(50);
    circle.setFillColor(sf::Color::Green);
    circle.setPosition(100, 50); // расположим круг в центре окна
    
    //Создаем объект Image
    Image heroimage;
    heroimage.loadFromFile("img/player.png");//загружаем в него файл
    //Создаем Texture
    Texture herotexture;//создаем объект Texture (текстура)
    herotexture.loadFromImage(heroimage);//передаем в него объект Image (изображения)
    //Создаем Sprite
    Sprite herosprite;//создаем объект Sprite(спрайт)
    herosprite.setTexture(herotexture);//передаём в него объект Texture (текстуры)
    herosprite.setPosition(0, 0);//задаем начальные координаты появления спрайта
    herosprite.setScale(4, 4);
    
    
    int t = 0;
    // Основной цикл
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
            
        }
        
        // Очищаем окно
        window.clear();
        
        if(t%15==0){
            int animFrame = ((int)t/200)%8;
            herosprite.setTextureRect(IntRect(animFrame*64,0,64, 64));
        }
        
        // Рисуем круг
        window.draw(circle);
        window.draw(herosprite);//выводим спрайт на экран

        // Отображаем изменения на экране
        window.display();
        t+=1;
    }

    return 0;
}

