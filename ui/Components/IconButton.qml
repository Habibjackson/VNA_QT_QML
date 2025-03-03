// IconButton.qml
import QtQuick
import QtQuick.Controls.Material
import QtQuick.Effects

Button {
    id: iconButton

    // Custom properties
    property url iconSource: "" // Path to the icon image
    property real iconSize: 24 // Size of the icon
    property color iconColor: "black" // Color of the icon
    property color hoverColor: "#222" // Background color on hover
    property color pressedColor: "transparent" // Background color when pressed
    property color activeColor: "#00cc00"

    property bool active: false
    // Customize the button's appearance
    background: Rectangle {
        id: bgRect
        implicitWidth: 100
        implicitHeight: 40
        color: iconButton.down ? pressedColor : (iconButton.hovered ? hoverColor : "transparent")
        radius: 4 // Rounded corners
    }

    contentItem: Column {
        spacing: 5 // Space between icon and text
        anchors.centerIn: parent

        // Icon
        Image {
            id: icon
            source: iconButton.iconSource
            width: iconButton.iconSize
            height: iconButton.iconSize
            anchors {
                centerIn: parent
            }
            sourceSize: Qt.size(iconButton.iconSize, iconButton.iconSize)
            visible: iconButton.iconSource.toString(
                         ) !== "" // Hide if no icon is provided
        }

        MultiEffect {
            source: icon
            anchors.fill: icon
            colorization: 1
            colorizationColor: iconButton.active ? iconButton.activeColor : (iconButton.hovered ? "#fff" : "transparent")
        }

        // Text
        Label {
            id: label
            text: iconButton.text
            font.pixelSize: 14
            color: iconButton.down ? "gray" : "black"
            visible: iconButton.text !== "" // Hide if no text is provided
            verticalAlignment: Text.AlignVCenter
        }
    }

    // Hover effect
    HoverHandler {
        id: hoverHandler
        enabled: true
    }
}
