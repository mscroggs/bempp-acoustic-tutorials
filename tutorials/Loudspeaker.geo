// Build a loudspeaker geometry
// Created by Jonathan Hargreaves of the University of Salford July 2021
//
// Developed for Gmsh version 4.8.4. The new OpenCASCADE kernel is utilised
// to allow creation of solid objects and boolean geometry operations.
// Hence this script will not work with earlier versions.

// Parameters:
CabinetHeight = 0.3;
CabinetWidth = 0.2;
CabinetDepth = 0.18;
CabinetChamferRadius = 0.015;
WooferRadius = 0.14/2;   // Note this is the radius it makes on the baffle
WooferDepth = WooferRadius/2; 
TweeterRadius = 0.02/2; // Note this is the radius it makes on the baffle
TweeterAngle = Pi/6;
PlotPlaneX = 0.6;
PlotPlaneY = 0.5;
PlotPlaneZ = 0.4;

// Use OpenCASCADE geometry kernel to allow solid geometry creation & boolean operations
SetFactory("OpenCASCADE");

// Create Loudspeaker cabinet:
Box(1) = {-CabinetHeight/2, -CabinetWidth/2, -CabinetDepth/2, CabinetHeight, CabinetWidth, CabinetDepth};
Fillet{1}{ Unique(Abs(Boundary{ Surface{Unique(Abs(Boundary{ Volume{1}; }))}; })) }{CabinetChamferRadius}

// Build object to subtract to make cone (indented into cabinet with an inverted dustcap):
Point(25) = {0, 0, 0};
Point(26) = {0, 0, -WooferDepth};
Point(27) = {WooferDepth^2/WooferRadius, 0, -Sqrt(WooferRadius^2 - WooferDepth^2)*WooferDepth/WooferRadius};
Point(28) = {WooferRadius, 0, 0};
Line(61) = {25,26};
Circle(62) = {26,25,27};
Line(63) = {27,28};
Line(64) = {28,25};
Line Loop(27) = {61,62,63,64};
Surface(27) = {27};
ExtrudedEntities[] = Extrude {{0, 0,  1}, {0, 0, 0},  2*Pi} { Surface{27}; };
Recursive Delete { Surface{27}; } // Delete original surface (which isn't part of the extrusion)
Translate {CabinetWidth/2 - CabinetHeight/2, 0, CabinetDepth/2} { Volume{2}; } // Move into the correct position
BooleanDifference(3) = { Volume{1}; Delete; } { Volume{2}; Delete; };

// Add tweeter (protruding dome):
Sphere(4) = {0, 0, -TweeterRadius/Tan(TweeterAngle), TweeterRadius/Sin(TweeterAngle), 0, Pi/2, 2*Pi};
Translate {CabinetWidth/2 - CabinetChamferRadius, 0, CabinetDepth/2} { Volume{4}; } // Move into the correct position
BooleanUnion(5) = { Volume{3}; Delete; }{ Volume{4}; Delete; };

// Create Physical Surfaces (used for boundary condition setting in bempp):
Physical Surface (1) = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28}; // Cabinet
Physical Surface (2) = {21, 29}; // Woofer
Physical Surface (3) = {22}; // Tweeter

// Set meshing options:
Mesh.MeshSizeMin = 0.01;
Mesh.MeshSizeMax = 0.02;

// The code below adds plotting planes. Uncomment it (remove "/*" and "*/" if you want to include this.

/*

// Add XZ Plotting Plane
Rectangle(30) = {-PlotPlaneX/2, 0, -CabinetDepth/2, PlotPlaneX/2 + CabinetWidth/2 - CabinetHeight/2, PlotPlaneZ};
Rectangle(31) = {CabinetWidth/2 - CabinetHeight/2, 0, -CabinetDepth/2, PlotPlaneX/2 - CabinetWidth/2 + CabinetHeight/2, PlotPlaneZ};
Rectangle(32) = {-CabinetHeight/2 - CabinetChamferRadius, -2*CabinetChamferRadius, -CabinetDepth/2, CabinetHeight+2*CabinetChamferRadius, CabinetDepth+3*CabinetChamferRadius, 2*CabinetChamferRadius};
BooleanDifference(33) = { Surface{30}; Delete; } { Surface{32}; };
BooleanDifference(34) = { Surface{31}; Delete; } { Surface{32}; Delete; };
Rotate{ { 1, 0, 0 }, { 0, 0, -CabinetDepth/2 }, Pi/2 } { Surface{33}; Surface{34}; }

// Add YZ Plotting Plane
Rectangle(35) = {0, -PlotPlaneY/2, -CabinetDepth/2, PlotPlaneZ, PlotPlaneY/2};
Rectangle(36) = {0, 0,             -CabinetDepth/2, PlotPlaneZ, PlotPlaneY/2};
Rectangle(37) = {-2*CabinetChamferRadius, -CabinetWidth/2 - CabinetChamferRadius, -CabinetDepth/2, CabinetWidth+2*CabinetChamferRadius, CabinetDepth+3*CabinetChamferRadius, 2*CabinetChamferRadius};
BooleanDifference(38) = { Surface{35}; Delete; } { Surface{37}; };
BooleanDifference(39) = { Surface{36}; Delete; } { Surface{37}; Delete; };
Rotate{ { 0, 1, 0 }, { 0, 0, -CabinetDepth/2 }, -Pi/2 } { Surface{38}; Surface{39}; }
Translate { CabinetWidth/2 - CabinetHeight/2, 0, 0 } { Surface{38}; Surface{39}; }

// Create Physical Surfaces (used for boundary condition setting in bempp):
Physical Surface (4) = {33, 34}; // Plotting plane XZ
Physical Surface (5) = {38, 39}; // Plotting plane YZ

*/