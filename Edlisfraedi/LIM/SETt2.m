

F = sort([9.8, 7.9, 11.1, 3.98, 2.56, 9.42, 7.34, 8.49, 7.67, 6.62]); % F [N]
x = sort([17.2, 15, 17.9, 20.9, 19, 19.5, 16.3, 21.5, 21.5, 17.8]); % x [m]



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