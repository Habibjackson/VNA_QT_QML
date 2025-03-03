// components/MainContent.qml
import QtQuick
import QtQuick.Controls
import "../pages"

Paper {
    id: mainContent
    property alias mainStack: stackView

    Column {
        anchors.fill: parent
        StackView {
            id: stackView
            // anchors.fill: parent
            width: parent.width
            height: parent.height
            initialItem: ManageAntenna {} // Set the initial page
        }
    }
}
