import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'my-dream-app';
  name : string;
  email; // : String;
  webpage: string;
  hobbies: string[];

  constructor(){
    this.name = "Sergio Danilo Hancco M.";
    this.email = "shanccom@unsa.edu.pe";
    this.webpage = "https//www.unsa.edu.pe";
    this.hobbies = ["voley","musica","bailar"];
    
  }
  showhobbies() {
    return true;
  }
}
