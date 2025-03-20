import QtQuick
import QtQuick.Controls

Item {
    id: lineBase
    property string text: ""
    // Horizontal line across the entire width
    Rectangle {
        id: line
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        width: parent.width
        height: 1
        color: "gray"
    }

    // Text overlapping the line
    Text {
        id: label
        text: lineBase.text
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        color: theme.textColor
        // Optionally, add a background rectangle to mask the line behind the text:
        Rectangle {
            anchors.fill: parent
            color: theme.paperBackground
            z: -1  // Ensure this background is behind the text
        }
    }
}
