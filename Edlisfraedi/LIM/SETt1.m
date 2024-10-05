
% Gögn úr töflunni
x = sort([13, 15, 14.5, 18.6, 16.2, 16.5, 17.2, 13.5, 15.5, 18.1]); % Lengd gormsins x [cm]

F = sort([5.587, 6.215, 9.303, 9.484, 5.653, 5.935, 8.641, 3.409, 8.69, 6.983]); % Kraftur F [N]


figure;
plot(x, F, 'o'); % Gögnin teiknuð með punktum og línu
xlabel('Lengd gormsins [cm]');
ylabel('Kraftur [N]');
grid on;

% Fylki með línulegri mátun á gögnin (hallatala = gormstuðull K)
p = polyfit(x, F, 1); % 1st gráðu margliða mátun

k_computed = p(1); % Hallatalan er gormstuðull K

% Sýna hallatöluna í skipanaglugganum
fprintf('Reiknaður gormstuðull K er: %.2f N/m\n', k_computed * 100);

% Bæta við mátunarlínu í grafinu
hold on;
x_fit = linspace(min(x), max(x), 100);
F_fit = polyval(p, x_fit);
plot(x_fit, F_fit, '--r'); % Línuleg mátun teiknuð með strikalínu
% legend('Gögn', 'Línuleg mátun');