import QtQuick
import QtQuick.Layouts
import "../Components"
import "../Widgets"

Paper {
    id: manageAntenna
    // anchors.fill: parent
    ColumnLayout {
        spacing: 10
        height: parent.height
        width: parent.width
        TitleBar {
            Layout.fillWidth: true
            color: "#003d01"
            title: qsTr("Manage Antenna's")
        }

        AntennaList {}
    }
}
