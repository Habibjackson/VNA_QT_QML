import QtQuick

QtObject {
    enum ThemeVariant {
        Light,
        Dark,
        Custom
    }

    property int currentTheme: Theme.Dark // Default: Dark theme

    // Common Colors
    readonly property color primaryColor: currentTheme === Theme.Dark ? "#1db954" : currentTheme === Theme.Custom ? "#FF9800" : "#6200EE"
    readonly property color secondaryColor: currentTheme === Theme.Dark ? "#03DAC6" : currentTheme === Theme.Custom ? "#4CAF50" : "#03A9F4"

    readonly property color backgroundColorGrey1: '#535353'
    readonly property color backgroundColorGrey2: '#b3b3b3'

    // Background Colors
    readonly property color backgroundColor: currentTheme === Theme.Dark ? "#000" : currentTheme === Theme.Custom ? "#FFF3E0" : "#FFFFFF"
    readonly property color cardColor: currentTheme
                                       === Theme.Dark ? "#212121" : currentTheme
                                                        === Theme.Custom ? "#FFE0B2" : "#000"
    readonly property color cardOpacity: currentTheme === Theme.Dark ? 0.4 : currentTheme === Theme.Custom ? "0.7" : "0.8"
    readonly property color barColor: currentTheme === Theme.Dark ? "#111" : currentTheme === Theme.Custom ? "#FFE0B2" : "#F5F5F5"

    // Elevation Shadows Per Theme
    readonly property color shadowColor: currentTheme === Theme.Dark ? "#40000000" : "#80000000"

    // paper
    readonly property color paperBackground: currentTheme === Theme.Dark ? "#111" : "#fff"

    // Text Colors
    readonly property color textColor: currentTheme
                                       === Theme.Dark ? "#eeeeee" : currentTheme
                                                        === Theme.Custom ? "#3E2723" : "#000000"

    // Button Colors
    readonly property color buttonColor: currentTheme === Theme.Dark ? "#3700B3" : currentTheme === Theme.Custom ? "#E65100" : "#6200EE"
    readonly property color buttonText: currentTheme === Theme.Dark ? "#FFFFFF" : currentTheme === Theme.Custom ? "#FFF8E1" : "#FFFFFF"
}
