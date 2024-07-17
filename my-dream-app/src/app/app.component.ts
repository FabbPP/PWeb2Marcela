import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule,RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'my-dream-app';
  name : string;
  email; // : String;
  webpage: string;
  hobbies: string[];
  showHobbies : boolean;

  constructor(){
    console.log ("Constructor working ...");
    this.name = "Sergio Danilo Hancco M.";
    this.email = "shanccom@unsa.edu.pe";
    this.webpage = "https//www.unsa.edu.pe";
    this.hobbies = ["voley","musica","bailar"];
    this.showHobbies = false;
    
  }
  toggleHobbies() {
    this.showHobbies = !this.showHobbies;
  }
  newHobby(hobby: HTMLInputElement) {
    this.hobbies.push(hobby.value);
    hobby.value = "";
    return false;
  }
}
