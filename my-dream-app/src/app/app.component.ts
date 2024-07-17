import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HelloWorldComponent} from "./hello-world/hello-world.component";
import { UserComponent } from "./user/user.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule,RouterOutlet,HelloWorldComponent, UserComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  users = ["Jaden", "Sergio", "Fabiana", "Aedo"];
  activated = false; 
}
