import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Item {
    property string title: ""
    property color color: "#fff"
    id: titleBar
    width: parent.width
    height: 48
    Rectangle {
        width: parent.width
        height: parent.height
        color: parent.color // Dark background
        topLeftRadius: 5
        topRightRadius: 5

        RowLayout {
            anchors.fill: parent
            anchors.margins: 12
            spacing: 8

            // Title Text
            Text {
                text: titleBar.title
                color: theme.textColor
                font.bold: true
                font.pixelSize: 28
                elide: Text.ElideRight
                verticalAlignment: Text.AlignVCenter
            }
        }
    }
}
