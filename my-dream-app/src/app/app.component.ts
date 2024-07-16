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
  name = "Fabiana Pacheco P.";
  email = "fpachecop@unsa.edu.pe";
  webpage = "https://www.unsa.edu.pe";
}
