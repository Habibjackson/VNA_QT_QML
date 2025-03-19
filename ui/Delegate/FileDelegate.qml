import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Item {
    width: parent.width
    height: 65 // Increased height for better spacing

    Rectangle {
        id: container
        width: parent.width - 20
        height: parent.height // Creates spacing between items
        radius: 8
        color: ListView.isCurrentItem ? theme.backgroundColorGrey1 : "transparent" // Alternating row colors
        border.width: 0
        anchors.horizontalCenter: parent.horizontalCenter

        // Hover effect
        MouseArea {
            anchors.fill: parent
            hoverEnabled: true
            onClicked: antennaManager.loadAntenna(model.filename)
            onEntered: () => {
                           container.color = theme.backgroundColorGrey1
                       }
            onExited: () => {
                          container.color = "transparent"
                      } // Restore original color
        }

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 4

            Text {
                text: model.filename
                font.bold: true
                Layout.fillWidth: true
                color: theme.textColor
            }
        }
    }
}
